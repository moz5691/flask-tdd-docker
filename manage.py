from flask.cli import FlaskGroup
from project import create_app, db
from project.api.users.models import User

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    db.session.add(User(username='michael', email="michael@email.com"))
    db.session.add(User(username='john', email="john@email.com"))
    db.session.commit()


if __name__ == '__main__':
    cli()
