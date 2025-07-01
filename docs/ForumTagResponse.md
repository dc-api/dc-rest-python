# ForumTagResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**moderated** | **bool** |  | 
**emoji_id** | **str** |  | [optional] 
**emoji_name** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.forum_tag_response import ForumTagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ForumTagResponse from a JSON string
forum_tag_response_instance = ForumTagResponse.from_json(json)
# print the JSON string representation of the object
print(ForumTagResponse.to_json())

# convert the object into a dict
forum_tag_response_dict = forum_tag_response_instance.to_dict()
# create an instance of ForumTagResponse from a dict
forum_tag_response_from_dict = ForumTagResponse.from_dict(forum_tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


