import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from .models.user import User as UserModel
from app import db

# Define a GraphQL type for the User model
class UserType(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (graphene.relay.Node, )

# Create a Query type
class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_users = graphene.List(UserType)

    def resolve_all_users(self, info):
        # Query to return all users
        return UserModel.query.all()

# Create a Mutation type for updating user info
class UpdateUserInfo(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int(required=True)
        name = graphene.String()
        email = graphene.String()
        profile_picture = graphene.String()

    user = graphene.Field(UserType)

    def mutate(self, info, user_id, name=None, email=None, profile_picture=None):
        user = UserModel.query.get(user_id)
        if user is None:
            raise Exception('No user with the given ID')

        if name:
            user.name = name
        if email:
            user.email = email
        if profile_picture:
            user.profile_picture = profile_picture
        # Add here additional fields if needed

        # Commit to the database
        db.session.commit()
        return UpdateUserInfo(user=user)

# Define the Mutation type
class Mutation(graphene.ObjectType):
    update_user_info = UpdateUserInfo.Field()

# Define the Schema
schema = graphene.Schema(query=Query, mutation=Mutation)
