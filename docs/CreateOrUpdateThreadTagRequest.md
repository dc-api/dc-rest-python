# CreateOrUpdateThreadTagRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**emoji_id** | **str** |  | [optional] 
**emoji_name** | **str** |  | [optional] 
**moderated** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.create_or_update_thread_tag_request import CreateOrUpdateThreadTagRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateThreadTagRequest from a JSON string
create_or_update_thread_tag_request_instance = CreateOrUpdateThreadTagRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOrUpdateThreadTagRequest.to_json())

# convert the object into a dict
create_or_update_thread_tag_request_dict = create_or_update_thread_tag_request_instance.to_dict()
# create an instance of CreateOrUpdateThreadTagRequest from a dict
create_or_update_thread_tag_request_from_dict = CreateOrUpdateThreadTagRequest.from_dict(create_or_update_thread_tag_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


