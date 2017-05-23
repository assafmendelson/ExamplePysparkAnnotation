from pyspark.sql import Column
import collections

def abs(col: Column) -> Column:
    """
    Computes the absolute value.

    New in version 1.3.
    """
    ...

def acos(col: Column) -> Column:
    """
    Computes the cosine inverse of the given value; the returned angle is in the range 0.0 through pi.

    New in version 1.4.
    """
    ...

def add_months(start: Column, months: int) -> Column:
    # when there is a specific "def" it inherits the docstring so we only need to add the type inference
    ...

def approxCountDistinct(col: Column, rsd: float) -> Column:
    # when there is a specific "def" it inherits the docstring so we only need to add the type inference
    ...

def array(*cols: collections.Iterable[Column] or collections.Iterable[str]) -> Column:
    # when there is a specific "def" it inherits the docstring so we only need to add the type inference
    ...

def asc(col: str) -> Column:
    """
    Returns a sort expression based on the ascending order of the given column name.

    New in version 1.3.
    """
    ...

def lit(col) -> Column:
    """
    Creates a Column of literal value.

    New in version 1.3.
    """
    ...

def col(col: str) -> Column:
    """
    Returns a Column based on the given column name.

    New in version 1.3.
    """
    ...

def column(col: str) -> Column:
    """
    Returns a Column based on the given column name.

    New in version 1.3.
    """

def desc(col: str) -> Column:
    """
    Returns a sort expression based on the descending order of the given column name.

    New in version 1.3.
    """
    ...


def upper(col: Column) -> Column:
    """
    Converts a string column to upper case.

    New in version 1.5.
    """
    ...

def lower(col: Column) -> Column:
    """
    Converts a string column to lower case.

    New in version 1.5.
    """
    ...

def sqrt(col: Column) -> Column:
    """
    Computes the square root of the specified float value.

    New in version 1.3.
    """
    ...


def max(col: Column) -> Column:
    """
    Aggregate function: returns the maximum value of the expression in a group.
    """
    ...

def min(col: Column) -> Column:
    """
    Aggregate function: returns the minimum value of the expression in a group.
    """
    ...

def count(col: Column) -> Column:
    """
    Aggregate function: returns the number of items in a group.
    """
    ...

def sum(col: Column) -> Column:
    """
    Aggregate function: returns the sum of all values in the expression.
    """
    ...

def avg(col: Column) -> Column:
    """
    Aggregate function: returns the average of the values in a group.
    """
    ...

def mean(col: Column) -> Column:
    """
    Aggregate function: returns the average of the values in a group.
    """
    ...

def sumDistinct(col: Column) -> Column:
    """
    Aggregate function: returns the sum of distinct values in the expression.
    """
    ...


def exp(col: Column) -> Column:
    """
    Computes the exponential of the given value.
    """
    ...
