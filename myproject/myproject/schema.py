import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
from graphql import GraphQLError


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ["id", "username"]


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    user_list = graphene.List(UserType)

    def resolve_user_list(root, info):
        raise GraphQLError("Let's add 'errors' to response 'data'.")


class DeleteOrderlineMutation(graphene.Mutation):
    Output = graphene.ID()

    class Arguments:
        line_id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, line_id):
        # Check something (whatever). Raise GraphQLError if request is not acceptable
        if str(line_id) == "42":
            raise GraphQLError(
                "Order mutation not allowed, Orderline can not be deleted."
            )

        # If check passes, do stuff. We don't do anything here.

        return line_id


class Mutation(graphene.ObjectType):
    delete_orderline = DeleteOrderlineMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
