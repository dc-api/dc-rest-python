# CreateEntitlementRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku_id** | **str** |  | 
**owner_id** | **str** |  | 
**owner_type** | **int** |  | 

## Example

```python
from dc_rest.models.create_entitlement_request_data import CreateEntitlementRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEntitlementRequestData from a JSON string
create_entitlement_request_data_instance = CreateEntitlementRequestData.from_json(json)
# print the JSON string representation of the object
print(CreateEntitlementRequestData.to_json())

# convert the object into a dict
create_entitlement_request_data_dict = create_entitlement_request_data_instance.to_dict()
# create an instance of CreateEntitlementRequestData from a dict
create_entitlement_request_data_from_dict = CreateEntitlementRequestData.from_dict(create_entitlement_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


