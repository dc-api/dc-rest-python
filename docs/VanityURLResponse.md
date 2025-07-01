# VanityURLResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**uses** | **int** |  | 
**error** | [**VanityURLErrorResponse**](VanityURLErrorResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.vanity_url_response import VanityURLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VanityURLResponse from a JSON string
vanity_url_response_instance = VanityURLResponse.from_json(json)
# print the JSON string representation of the object
print(VanityURLResponse.to_json())

# convert the object into a dict
vanity_url_response_dict = vanity_url_response_instance.to_dict()
# create an instance of VanityURLResponse from a dict
vanity_url_response_from_dict = VanityURLResponse.from_dict(vanity_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


