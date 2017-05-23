from pyspark.sql import Column

class Column:
    def __mul__(self, other) -> Column:
        pass

    def __rmul__(self, other) -> Column:
        pass

class DataFrame:
    def __getitem__(self, item) -> Column:
        pass

    def __getattr__(self, name) -> Column:
        pass