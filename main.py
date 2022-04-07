from operator import le
from process import customerProcessing
from constants import querystring

def main():
    customer = customerProcessing(querystring)
    print("Job completed:", len(customer))
    
main()