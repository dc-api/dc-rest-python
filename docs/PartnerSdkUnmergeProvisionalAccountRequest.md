# PartnerSdkUnmergeProvisionalAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**client_secret** | **str** |  | [optional] 
**external_auth_token** | **str** |  | 
**external_auth_type** | **str** |  | 

## Example

```python
from dc_rest.models.partner_sdk_unmerge_provisional_account_request import PartnerSdkUnmergeProvisionalAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerSdkUnmergeProvisionalAccountRequest from a JSON string
partner_sdk_unmerge_provisional_account_request_instance = PartnerSdkUnmergeProvisionalAccountRequest.from_json(json)
# print the JSON string representation of the object
print(PartnerSdkUnmergeProvisionalAccountRequest.to_json())

# convert the object into a dict
partner_sdk_unmerge_provisional_account_request_dict = partner_sdk_unmerge_provisional_account_request_instance.to_dict()
# create an instance of PartnerSdkUnmergeProvisionalAccountRequest from a dict
partner_sdk_unmerge_provisional_account_request_from_dict = PartnerSdkUnmergeProvisionalAccountRequest.from_dict(partner_sdk_unmerge_provisional_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


