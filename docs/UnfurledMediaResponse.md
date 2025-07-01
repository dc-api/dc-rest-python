# UnfurledMediaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**url** | **str** |  | 
**proxy_url** | **str** |  | 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 
**content_type** | **str** |  | [optional] 
**attachment_id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.unfurled_media_response import UnfurledMediaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnfurledMediaResponse from a JSON string
unfurled_media_response_instance = UnfurledMediaResponse.from_json(json)
# print the JSON string representation of the object
print(UnfurledMediaResponse.to_json())

# convert the object into a dict
unfurled_media_response_dict = unfurled_media_response_instance.to_dict()
# create an instance of UnfurledMediaResponse from a dict
unfurled_media_response_from_dict = UnfurledMediaResponse.from_dict(unfurled_media_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


