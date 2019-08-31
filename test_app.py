import unittest

from app import render_csv


CSV_BY_RENDERED_TWTXT = {
    # Simple example
    "25/08/2019 10:10:00,Hello World!": "2019-08-25T10:11:00+0000\tHello World!",
    # It's OK for commas to be in the csv
    "25/08/2019 10:10:00,\"Hello, World!\"": "2019-08-25T10:11:00+0000\tHello, World!",
    # Unwritten message (without a timestamp, we shouldn't post anything)
    "25/08/2019 10:10:00,Hello World!\n,Test": "2019-08-25T10:11:00+0000\tHello World!",
    # Extra columns shouldn't be printed
    "25/08/2019 10:10:00,Hello World!,More content": "2019-08-25T10:11:00+0000\tHello World!",
}


class TestRenderingCSV(unittest.TestCase):
    def test_render_csv(self):
        for csv, rendered_twtxt in CSV_BY_RENDERED_TWTXT.items():
            result = render_csv(csv)
            assert result == rendered_twtxt


if __name__ == "__main__":
    unittest.main()
