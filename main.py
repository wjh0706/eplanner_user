from app import create_app
from app import db
from flask_graphql import GraphQLView
from app.schema import schema

app = create_app()

with app.app_context():
    db.create_all()

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Enables the GraphiQL interface
    )
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8012, debug=True)