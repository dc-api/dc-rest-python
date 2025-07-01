# UpdateThreadRequestPartial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**archived** | **bool** |  | [optional] 
**locked** | **bool** |  | [optional] 
**invitable** | **bool** |  | [optional] 
**auto_archive_duration** | **int** |  | [optional] 
**rate_limit_per_user** | **int** |  | [optional] 
**flags** | **int** |  | [optional] 
**applied_tags** | **List[str]** |  | [optional] 
**bitrate** | **int** |  | [optional] 
**user_limit** | **int** |  | [optional] 
**rtc_region** | **str** |  | [optional] 
**video_quality_mode** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.update_thread_request_partial import UpdateThreadRequestPartial

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateThreadRequestPartial from a JSON string
update_thread_request_partial_instance = UpdateThreadRequestPartial.from_json(json)
# print the JSON string representation of the object
print(UpdateThreadRequestPartial.to_json())

# convert the object into a dict
update_thread_request_partial_dict = update_thread_request_partial_instance.to_dict()
# create an instance of UpdateThreadRequestPartial from a dict
update_thread_request_partial_from_dict = UpdateThreadRequestPartial.from_dict(update_thread_request_partial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


