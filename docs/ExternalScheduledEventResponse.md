# ExternalScheduledEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**guild_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**creator_id** | **str** |  | [optional] 
**creator** | [**UserResponse**](UserResponse.md) |  | [optional] 
**image** | **str** |  | [optional] 
**scheduled_start_time** | **datetime** |  | 
**scheduled_end_time** | **datetime** |  | [optional] 
**status** | **int** |  | 
**entity_type** | **int** |  | 
**entity_id** | **str** |  | [optional] 
**user_count** | **int** |  | [optional] 
**privacy_level** | **object** |  | 
**user_rsvp** | [**ScheduledEventUserResponse**](ScheduledEventUserResponse.md) |  | [optional] 
**entity_metadata** | [**EntityMetadataExternalResponse**](EntityMetadataExternalResponse.md) |  | 

## Example

```python
from dc_rest.models.external_scheduled_event_response import ExternalScheduledEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalScheduledEventResponse from a JSON string
external_scheduled_event_response_instance = ExternalScheduledEventResponse.from_json(json)
# print the JSON string representation of the object
print(ExternalScheduledEventResponse.to_json())

# convert the object into a dict
external_scheduled_event_response_dict = external_scheduled_event_response_instance.to_dict()
# create an instance of ExternalScheduledEventResponse from a dict
external_scheduled_event_response_from_dict = ExternalScheduledEventResponse.from_dict(external_scheduled_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


