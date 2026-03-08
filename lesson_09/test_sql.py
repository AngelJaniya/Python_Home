from sqlalchemy import create_engine, text


db_connection_string = (
        "postgresql://postgres:postgres@localhost:5432/university")
db = create_engine(db_connection_string)


def get_subject():
    connection = db.connect()
    result = connection.execute(
            text("SELECT * FROM subject WHERE subject_id = :id"), {'id': 777})
    rows = result.mappings().all()
    connection.close()
    return rows


def insert_subject():
    connection = db.connect()
    sql = 'INSERT INTO subject(subject_id, subject_title) values (:id, :title)'
    connection.execute(
            text(sql),
            {'id': 777, 'title': 'Magick'})
    connection.close()


def update_subject():
    connection = db.connect()
    sql = 'UPDATE subject SET subject_title = :title WHERE subject_id = :id'
    connection.execute(
            text(sql),
            {'id': 777, 'title': 'Thaumaturgy'})
    connection.close()


def delete_subject():
    connection = db.connect()
    connection.execute(
            text('DELETE FROM subject WHERE subject_id = :id'),
            {'id': 777})
    connection.close()


def test_insert():
    insert_subject()
    rows = get_subject()
    delete_subject()
    assert rows[0]['subject_title'] == 'Magick'


def test_update():
    insert_subject()
    update_subject()
    rows = get_subject()
    delete_subject()
    assert rows[0]['subject_title'] == 'Thaumaturgy'


def test_delete():
    insert_subject()
    delete_subject()
    rows = get_subject()
    assert len(rows) == 0
