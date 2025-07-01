# ThreadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **int** |  | 
**last_message_id** | **str** |  | [optional] 
**flags** | **int** |  | 
**last_pin_timestamp** | **datetime** |  | [optional] 
**guild_id** | **str** |  | 
**name** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**rate_limit_per_user** | **int** |  | [optional] 
**bitrate** | **int** |  | [optional] 
**user_limit** | **int** |  | [optional] 
**rtc_region** | **str** |  | [optional] 
**video_quality_mode** | **int** |  | [optional] 
**permissions** | **str** |  | [optional] 
**owner_id** | **str** |  | 
**thread_metadata** | [**ThreadMetadataResponse**](ThreadMetadataResponse.md) |  | [optional] 
**message_count** | **int** |  | 
**member_count** | **int** |  | 
**total_message_sent** | **int** |  | 
**applied_tags** | **List[str]** |  | [optional] 
**member** | [**ThreadMemberResponse**](ThreadMemberResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.thread_response import ThreadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadResponse from a JSON string
thread_response_instance = ThreadResponse.from_json(json)
# print the JSON string representation of the object
print(ThreadResponse.to_json())

# convert the object into a dict
thread_response_dict = thread_response_instance.to_dict()
# create an instance of ThreadResponse from a dict
thread_response_from_dict = ThreadResponse.from_dict(thread_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


