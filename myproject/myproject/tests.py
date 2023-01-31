from http import HTTPStatus

import pytest
from django.contrib.auth.models import User
from graphene_django.utils.testing import graphql_query

pytestmark = pytest.mark.django_db()


def test_query_hello():
    response = graphql_query("query { hello }")
    assert response.status_code == HTTPStatus.OK
    content = response.json()
    assert content["data"]["hello"] == "Hi!"


def test_query_user_list():
    response = graphql_query("query {userList { id username } }")
    assert response.status_code == HTTPStatus.OK
    content = response.json()
    assert content["errors"] == [
        {
            "locations": [{"column": 8, "line": 1}],
            "message": "Let's add 'errors' to response 'data'.",
            "path": ["userList"],
        },
    ]


def test_query_delete_orderline_mutation():
    response = graphql_query("mutation DeleteOrderline {deleteOrderline(lineId: 1)}")
    assert response.status_code == HTTPStatus.OK
    content = response.json()
    assert content["data"] == {"deleteOrderline": "1"}

    response = graphql_query("mutation DeleteOrderline {deleteOrderline(lineId: 42)}")
    assert response.status_code == HTTPStatus.OK
    content = response.json()
    assert (
        content["errors"][0]["message"]
        == "Order mutation not allowed, Orderline can not be deleted."
    )
    # Instead, this returns:
    # {
    #     "data": {
    #         "deleteOrderline": "<Promise at 0x7f42c0c11bd0 rejected with GraphQLError('Order mutation not allowed, Orderline can not be deleted.')>"
    #     }
    # }
