"""Unit tests for strategy pattern sample."""

import pytest

from samples.dsa.strategy_pattern.strategy import (
    BubbleSort,
    FileExporter,
    FlatDiscount,
    MergeSort,
    NoDiscount,
    PercentageDiscount,
    PriceCalculator,
    Sorter,
    gzip_compress,
    no_compress,
    zlib_compress,
)


@pytest.mark.unit
def test_bubble_sort():
    """Test BubbleSort strategy."""
    sorter = BubbleSort()
    data = [5, 3, 8, 1, 9, 2]
    result = sorter.sort(data)
    assert result == [1, 2, 3, 5, 8, 9]


@pytest.mark.unit
def test_bubble_sort_empty():
    """Test BubbleSort with empty list."""
    sorter = BubbleSort()
    result = sorter.sort([])
    assert result == []


@pytest.mark.unit
def test_merge_sort():
    """Test MergeSort strategy."""
    sorter = MergeSort()
    data = [5, 3, 8, 1, 9, 2]
    result = sorter.sort(data)
    assert result == [1, 2, 3, 5, 8, 9]


@pytest.mark.unit
def test_merge_sort_empty():
    """Test MergeSort with empty list."""
    sorter = MergeSort()
    result = sorter.sort([])
    assert result == []


@pytest.mark.unit
def test_sorter_strategy_swap():
    """Test swapping strategies at runtime."""
    data = [5, 3, 8, 1, 9, 2]
    sorter = Sorter(BubbleSort())
    result1 = sorter.sort(data)

    sorter.set_strategy(MergeSort())
    result2 = sorter.sort(data)

    assert result1 == result2 == [1, 2, 3, 5, 8, 9]


@pytest.mark.unit
def test_no_discount():
    """Test NoDiscount strategy."""
    discount = NoDiscount()
    assert discount.apply(100) == 100


@pytest.mark.unit
def test_percentage_discount():
    """Test PercentageDiscount strategy."""
    discount = PercentageDiscount(20)
    assert discount.apply(100) == 80.0


@pytest.mark.unit
def test_percentage_discount_50_percent():
    """Test PercentageDiscount with 50%."""
    discount = PercentageDiscount(50)
    assert discount.apply(100) == 50.0


@pytest.mark.unit
def test_flat_discount():
    """Test FlatDiscount strategy."""
    discount = FlatDiscount(15)
    assert discount.apply(100) == 85.0


@pytest.mark.unit
def test_flat_discount_more_than_price():
    """Test FlatDiscount with amount greater than price."""
    discount = FlatDiscount(150)
    assert discount.apply(100) == 0.0


@pytest.mark.unit
def test_price_calculator_strategy_swap():
    """Test swapping discount strategies."""
    calc = PriceCalculator(NoDiscount())
    assert calc.calculate(100) == 100

    calc.set_strategy(PercentageDiscount(20))
    assert calc.calculate(100) == 80.0


@pytest.mark.unit
def test_no_compress():
    """Test no compression strategy."""
    data = b"hello world"
    result = no_compress(data)
    assert result == data


@pytest.mark.unit
def test_gzip_compress():
    """Test gzip compression strategy."""
    data = b"hello world" * 100
    result = gzip_compress(data)
    assert len(result) < len(data)  # compression should reduce size


@pytest.mark.unit
def test_zlib_compress():
    """Test zlib compression strategy."""
    data = b"hello world" * 100
    result = zlib_compress(data)
    assert len(result) < len(data)  # compression should reduce size


@pytest.mark.unit
def test_file_exporter_strategy_swap():
    """Test swapping compression strategies."""
    data = b"hello world" * 100
    exporter = FileExporter(no_compress)
    result1 = exporter.export(data)

    exporter.set_strategy(gzip_compress)
    result2 = exporter.export(data)

    assert len(result2) < len(result1)
