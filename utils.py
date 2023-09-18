import pprint

from moysklad.queries import Expand, Filter, Ordering, Select, Search, Query

from config import client, methods


def get_categories():
    response = client.get(
        method=methods.get_list_url('productfolder'),
        query=Query(
            Filter(),
            Ordering().asc('pathName'),
            Select(limit=100),
        ),
    )
    category = {}
    for row in response.rows:
        if row['pathName'] == "":
            category[row['name']] = []
        else:
            category[row['pathName']].append(
                {
                    "id": row["id"],
                    "name": row['name'],
                }
            )

    return category


def get_products(path_id):
    path_id="66e2f163-2303-11ee-0a80-08ce000b3a10"
    response = client.get(
        method=methods.get_list_url('product'),
        query=Query(
            Filter(),
            Expand("stock.quantity"),
            Ordering().asc('name'),
            Select(limit=10),
        ),
    )
    print(response.meta)
    print(response.context)
    pprint.pprint(response.rows)


def daun():
    response = client.get(
        method=methods.get_list_url('counterparty'),
        query=Query(
            Filter().exists('email=123').eq('archived', False),
            Search('петров'),
            Expand('owner', 'owner.group'),
            Ordering().asc('id').desc('name'),
            Select(limit=1),
        ),
    )
    print(response.meta)
    print(response.context)
    print(response.rows)