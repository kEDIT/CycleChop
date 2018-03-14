import unittest

from cyclechop.sample import run

#@unittest.skip("TODO: Implement Schema")
class TestSchema(unittest.TestCase):
    def setUp(self):
        import pandas as pd
        #Import csv file as a dataframe
        TEST_INPUT_DIR="./resources/autoclave\ tribo/"
        test_file_name="HPAr-autoclave\ test-180302.csv"
        self.fixture = pd.read_csv(TEST_INPUT_DIR + test_file_name,sep=',',header=0)
        print(self.fixture)
    
    def tearDown(self):
        del(self.fixture)
    
    @unittest.skip("TODO: Exception raised")
    def test_schema_smoke_exception(self):
        """
        Schema class constructor smoke test.
        
        Should raise an exception since Schema() constructor is called without any arguments
        """
        unittest.assertRaises(Exception,run.Schema())
    
    # def test_schema_from_df(self):
        # schema = Schema(df=self.fixture)
            


