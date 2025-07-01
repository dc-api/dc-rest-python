# ProvisionalTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_type** | **str** |  | 
**access_token** | **str** |  | 
**expires_in** | **int** |  | 
**scope** | **str** |  | 
**id_token** | **str** |  | 
**refresh_token** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**expires_at_s** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.provisional_token_response import ProvisionalTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisionalTokenResponse from a JSON string
provisional_token_response_instance = ProvisionalTokenResponse.from_json(json)
# print the JSON string representation of the object
print(ProvisionalTokenResponse.to_json())

# convert the object into a dict
provisional_token_response_dict = provisional_token_response_instance.to_dict()
# create an instance of ProvisionalTokenResponse from a dict
provisional_token_response_from_dict = ProvisionalTokenResponse.from_dict(provisional_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


