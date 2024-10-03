"""
Module: ebs-pricing.py

This module contains functions for calculating pricing related to Amazon Elastic Block Store (EBS).
"""
# WIP - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing.html
# https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/eu-west-1/index.json
# https://github.com/lyft/awspricing

def get_ebs_storage_price(region):
    # WIP
    pricing = boto3.client('pricing', region_name=region,
                       aws_access_key_id='xxxxxxxxxxxxxxxxxxxxxxxxx',
aws_secret_access_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
aws_session_token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
)

response = pricing.describe_services()
service_codes = [service['ServiceCode'] for service in response['Services']]
all_prices = []

for service_code in service_codes:
    print(f"Fetching prices for service: {service_code}")
    paginator = pricing.get_paginator('get_products')

    for page in paginator.paginate(ServiceCode=service_code):
        for price_item in page['PriceList']:
            all_prices.append(price_item)

    print(response)

def main():
    # WIP
    get_ebs_storage_price('us-east-1')

if __name__ == "__main__":
    main()
