from __future__ import annotations

import sqlite3

DB_PATH = ':memory:'

TASK_DONE_SYMBOL = '[X]'
TASK_PENDING_SYMBOL = '[ ]'


def create_db(db_path: str = DB_PATH) -> None:
    """Crea la base de datos en la ruta db_path y la tabla 'tasks'."""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = """CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        done INTEGER
    )"""
    cur.execute(sql)
    con.commit()
    con.close()

class _AutoCloseConnection(sqlite3.Connection):
    """Conexión que se cierra sola al destruirse, para no bloquear
    el fichero de la base de datos en Windows."""
    def __del__(self) -> None:
        try:
            self.close()
        except Exception:
            pass

def _connect(db_path: str = DB_PATH) -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    con = sqlite3.connect(db_path, factory=_AutoCloseConnection)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    return con, cur

class Task:
    # 2.1 Atributos de clase
    con, cur = _connect(DB_PATH)

    def __init__(self, name: str, done: bool = False, id: int = -1):
        self.name = name
        self.done = done
        self.id = id

    def save(self) -> None:
        """Inserta la tarea self en la base de datos y actualiza self.id."""
        sql = "INSERT INTO tasks (name, done) VALUES (?, ?)"
        self.cur.execute(sql, (self.name, int(self.done)))
        self.con.commit()
        if self.cur.lastrowid is not None:
            self.id = self.cur.lastrowid

    def update(self) -> None:
        """Actualiza la tarea self en la base de datos (nombre y estado)."""
        sql = "UPDATE tasks SET name = ?, done = ? WHERE id = ?"
        self.cur.execute(sql, (self.name, int(self.done), self.id))
        self.con.commit()

    def check(self) -> None:
        """Marca la tarea como completada usando update()."""
        self.done = True
        self.update()

    def uncheck(self) -> None:
        """Marca la tarea como no completada usando update()."""
        self.done = False
        self.update()

    def __repr__(self) -> str:
        """Devuelve [X] <name> (id=<id>) o [ ] <name> (id=<id>)."""
        status = TASK_DONE_SYMBOL  if self.done else TASK_PENDING_SYMBOL 
        return f"{status} {self.name} (id={self.id})"

    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> Self:
        """Construye y devuelve una nueva tarea a partir de una fila sqlite3.Row."""
        return cls(
            name=row["name"],
            done=bool(row["done"]),
            id=row["id"],
        )

    @classmethod
    def get(cls, task_id: int) -> Optional[Self]:
        """Obtiene una tarea de la base de datos por su ID usando from_db_row()."""
        sql = "SELECT * FROM tasks WHERE id = ?"
        cls.cur.execute(sql, (task_id,))
        row = cls.cur.fetchone()

        if row is None:
            return None

        return cls.from_db_row(row)


class ToDo:
    # 3.1 Atributos de clase
    con, cur = _connect(DB_PATH)

    def get_tasks(self, done: int = -1) -> Generator[Task, None, None]:
        """Función generadora que devuelve tareas como objetos Task."""
        if done == -1:
            sql = "SELECT * FROM tasks"
            self.cur.execute(sql)
        else:
            sql = "SELECT * FROM tasks WHERE done = ?"
            self.cur.execute(sql, (done,))

        rows = self.cur.fetchall()
        for row in rows:
            """
            Cuando una función contiene yield, llamarla no ejecuta 
            su código inmediatamente. En vez de eso, devuelve un 
            objeto generador — una especie de "receta pendiente de 
            cocinar" — y el cuerpo de la función solo se va ejecutando 
            poco a poco, un yield cada vez, según se le va pidiendo 
            el siguiente valor (con un for, con next(), o metiéndolo 
            en list(...), etc.).
            Ventajas:
            En este caso concreto, la ventaja principal es conceptual
            y de diseño: get_tasks representa "dame las tareas, una a una,
            según las vayas necesitando", lo cual es el patrón correcto 
            para cualquier consulta a base de datos, independientemente de 
            si internamente usa fetchall() o algo más incremental como 
            fetchone() en bucle. Si en el futuro decidieras optimizar 
            la implementación para leer fila a fila directamente de SQLite
            en vez de traerlas todas con fetchall(), la interfaz pública 
            no cambiaría — seguiría siendo un generador que se usa igual con 
            for tarea in todo.get_tasks(): — mientras que si hubiera devuelto 
            una lista, cambiar la implementación interna sí podría afectar 
            a quien la usa (por ejemplo, si alguien dependiera de poder indexar 
            el resultado con tareas[0], cosa que un generador no permite).
            """
            yield Task.from_db_row(row)

    def add_task(self, name: str) -> None:
        """Añade una tarea usando la clase Task y sus métodos."""
        task = Task(name=name)
        task.save()

    def complete_task(self, task_id: int) -> None:
        """Marca la tarea como completada usando la clase Task."""
        task = Task.get(task_id)
        if task:
            task.check()

    def reopen_task(self, task_id: int) -> None:
        """Marca la tarea como pendiente usando la clase Task."""
        task = Task.get(task_id)
        if task:
            task.uncheck()
