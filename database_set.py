import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS targets (
    id INTEGER PRIMARY KEY,
    kalori INTEGER NOT NULL,
    protein INTEGER NOT NULL
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_workout TEXT NOT NULL
)
""")


# Tabel progress harian
cursor.execute("""
CREATE TABLE IF NOT EXISTS progress_harian (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session TEXT NOT NULL,
    nama_workout TEXT,
    kalori INTEGER NOT NULL,
    protein INTEGER NOT NULL,
    status TEXT NOT NULL,
    target_kalori INTEGER DEFAULT 0,
    target_protein INTEGER DEFAULT 0
)
""")
conn.commit()


cursor.execute("SELECT COUNT(*) FROM targets")
if cursor.fetchone()[0] == 0:
    cursor.execute("INSERT INTO targets (id, kalori, protein) VALUES (1, 0, 0)")
    conn.commit()


def insert_target_workout(workout):
    cursor.execute("INSERT INTO workouts (nama_workout) VALUES (?)", (workout,))
    conn.commit()

def delete_workout_by_id(workout_id):
    cursor.execute("DELETE FROM workouts WHERE id = ?", (workout_id,))
    conn.commit()

def insert_target_kalori(kalori):
    cursor.execute("UPDATE targets SET kalori = ?", (kalori,))
    conn.commit()

def insert_target_protein(protein):
    cursor.execute("UPDATE targets SET protein = ?", (protein,))
    conn.commit()

def get_target():
    cursor.execute("SELECT kalori, protein FROM targets WHERE id = 1")
    return cursor.fetchone()

def get_workouts():
    cursor.execute("SELECT id, nama_workout FROM workouts ORDER BY id")
    return cursor.fetchall()

def get_session():
    cursor.execute("SELECT session FROM progress_harian")
    return cursor.fetchall()

def insert_progress(session, nama_workout, kalori, protein, status):
    target_kal, target_pro = get_target()
    
    cursor.execute("""
        INSERT INTO progress_harian 
        (session, nama_workout, status, kalori, protein, target_kalori, target_protein)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (session, nama_workout, status, kalori, protein, target_kal, target_pro))
    
    conn.commit()

def get_progress_history():
    cursor.execute("""
        SELECT session,
               GROUP_CONCAT(nama_workout || ' ' || status, '\n') AS daftar_workout,
               MAX(kalori),
               MAX(target_kalori),
               MAX(protein),
               MAX(target_protein)
        FROM progress_harian
        GROUP BY session
        ORDER BY id DESC
    """)
    return cursor.fetchall()