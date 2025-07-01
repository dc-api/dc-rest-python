# ThreadMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**join_timestamp** | **datetime** |  | 
**flags** | **int** |  | 
**member** | [**GuildMemberResponse**](GuildMemberResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.thread_member_response import ThreadMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadMemberResponse from a JSON string
thread_member_response_instance = ThreadMemberResponse.from_json(json)
# print the JSON string representation of the object
print(ThreadMemberResponse.to_json())

# convert the object into a dict
thread_member_response_dict = thread_member_response_instance.to_dict()
# create an instance of ThreadMemberResponse from a dict
thread_member_response_from_dict = ThreadMemberResponse.from_dict(thread_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


