# StageScheduledEventCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**scheduled_start_time** | **datetime** |  | 
**scheduled_end_time** | **datetime** |  | [optional] 
**privacy_level** | **object** |  | 
**entity_type** | **int** |  | 
**channel_id** | **str** |  | [optional] 
**entity_metadata** | **object** |  | [optional] 

## Example

```python
from dc_rest.models.stage_scheduled_event_create_request import StageScheduledEventCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StageScheduledEventCreateRequest from a JSON string
stage_scheduled_event_create_request_instance = StageScheduledEventCreateRequest.from_json(json)
# print the JSON string representation of the object
print(StageScheduledEventCreateRequest.to_json())

# convert the object into a dict
stage_scheduled_event_create_request_dict = stage_scheduled_event_create_request_instance.to_dict()
# create an instance of StageScheduledEventCreateRequest from a dict
stage_scheduled_event_create_request_from_dict = StageScheduledEventCreateRequest.from_dict(stage_scheduled_event_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


