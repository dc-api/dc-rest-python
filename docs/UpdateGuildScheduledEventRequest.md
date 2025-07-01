# UpdateGuildScheduledEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**scheduled_start_time** | **datetime** |  | [optional] 
**scheduled_end_time** | **datetime** |  | [optional] 
**entity_type** | **int** |  | [optional] 
**privacy_level** | **object** |  | [optional] 
**channel_id** | **str** |  | [optional] 
**entity_metadata** | **object** |  | [optional] 

## Example

```python
from dc_rest.models.update_guild_scheduled_event_request import UpdateGuildScheduledEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGuildScheduledEventRequest from a JSON string
update_guild_scheduled_event_request_instance = UpdateGuildScheduledEventRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGuildScheduledEventRequest.to_json())

# convert the object into a dict
update_guild_scheduled_event_request_dict = update_guild_scheduled_event_request_instance.to_dict()
# create an instance of UpdateGuildScheduledEventRequest from a dict
update_guild_scheduled_event_request_from_dict = UpdateGuildScheduledEventRequest.from_dict(update_guild_scheduled_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


