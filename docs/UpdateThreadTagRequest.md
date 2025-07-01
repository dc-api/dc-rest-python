# UpdateThreadTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**emoji_id** | **str** |  | [optional] 
**emoji_name** | **str** |  | [optional] 
**moderated** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.update_thread_tag_request import UpdateThreadTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateThreadTagRequest from a JSON string
update_thread_tag_request_instance = UpdateThreadTagRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateThreadTagRequest.to_json())

# convert the object into a dict
update_thread_tag_request_dict = update_thread_tag_request_instance.to_dict()
# create an instance of UpdateThreadTagRequest from a dict
update_thread_tag_request_from_dict = UpdateThreadTagRequest.from_dict(update_thread_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


