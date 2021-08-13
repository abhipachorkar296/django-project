import requests
import json

def post_draft_bid(event_id=1):
    base_url = "http://127.0.0.1:8000/event"
    endpoint = "/draft_bid_list/"+str(event_id)


    abs_url = base_url+endpoint

    draft_bids = {
        "bid_info":
        {
            "event_id" : 1,
            "bid_creator_user_id" : 1, 
            "bid_creator_entity_type" : "S", 
            "buyer_id" : 1,
            "seller_id" : 3,
            "seller_bid_id" : "12345",
            "bid_creation_datetime" : "2021-08-02T06:03:08.583002Z",
            "bid_valid_till_datetime" : "2021-08-04T06:03:08.583002Z",
            "payment_terms_code" : "xyz",
            "seller_comments": "not good",
            "rebid_request_comments" : "new",
            "currency_code" : "USD",
            "subtotal" : 100,
            "taxes" : 12,
            "total_shipping_cost" :14,
            "total_other_charges" : 16,
            "bulk_discount_percentage" : 1,
            "bulk_discount_amount" :1,
            "total" : 200,
            "status" : "Response submitted"
        },
        "bid_item_list" :
        [
            {
                "item_info":
                {
                    "event_line_item_id" : 1,
                    "measurement_unit_id" : 1,
                    "quantity_offered" : 100.00,
                    "quantity_awarded" : 100.00, 
                    "currency_code" : "USD",
                    "price" : 0.01,
                    "other_charges" : 50, 
                    "shipping_managed_by" : "S",
                    "shipping_cost" : 1,
                    "total_amount" : 1,
                    "seller_comments" : "ll" 
                },
                "item_tax":
                [
                    {
                        "tax_name" : "ll",
                        "value" : 1
                    }
                ]
            }
        ]
    }
    headers = {
        'Content-Type': 'application/json'
    }
    
    # for draft_bid in draft_bids:
    #     response = requests.post(abs_url, draft_bid)
    #     print(response.status_code)
    response = requests.post(abs_url, json.dumps(draft_bids), headers=headers)
    print(response.status_code)

post_draft_bid(1)