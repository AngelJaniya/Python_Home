from sqlalchemy import create_engine, text

db_connection_string = (
    "postgresql://postgres:postgres@localhost:5432/university"
)
db = create_engine(db_connection_string)


def get_subject():
    with db.connect() as connection:
        result = connection.execute(
            text("SELECT * FROM subject WHERE subject_id = :id"),
            {'id': 777}
        )
        return result.mappings().all()


def insert_subject():
    with db.connect() as connection:
        sql = (
            'INSERT INTO subject(subject_id, subject_title) '
            'values (:id, :title)'
        )
        connection.execute(
            text(sql),
            {'id': 777, 'title': 'Magick'}
        )
        connection.commit()


def update_subject():
    with db.connect() as connection:
        sql = (
            'UPDATE subject SET subject_title = :title '
            'WHERE subject_id = :id'
        )
        connection.execute(
            text(sql),
            {'id': 777, 'title': 'Thaumaturgy'}
        )
        connection.commit()


def delete_subject():
    with db.connect() as connection:
        connection.execute(
            text('DELETE FROM subject WHERE subject_id = :id'),
            {'id': 777}
        )
        connection.commit()
