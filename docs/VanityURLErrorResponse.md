# VanityURLErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**code** | **int** |  | 

## Example

```python
from dc_rest.models.vanity_url_error_response import VanityURLErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VanityURLErrorResponse from a JSON string
vanity_url_error_response_instance = VanityURLErrorResponse.from_json(json)
# print the JSON string representation of the object
print(VanityURLErrorResponse.to_json())

# convert the object into a dict
vanity_url_error_response_dict = vanity_url_error_response_instance.to_dict()
# create an instance of VanityURLErrorResponse from a dict
vanity_url_error_response_from_dict = VanityURLErrorResponse.from_dict(vanity_url_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


