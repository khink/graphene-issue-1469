Illustration of https://github.com/graphql-python/graphene/issues/1469:

    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    cd myproject
    pytest

If you look in [tests.py](./myproject/myproject/tests.py), you'll see the last test fails.
