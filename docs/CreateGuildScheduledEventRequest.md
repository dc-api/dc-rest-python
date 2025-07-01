# CreateGuildScheduledEventRequest


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
**entity_metadata** | **object** |  | 

## Example

```python
from dc_rest.models.create_guild_scheduled_event_request import CreateGuildScheduledEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGuildScheduledEventRequest from a JSON string
create_guild_scheduled_event_request_instance = CreateGuildScheduledEventRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGuildScheduledEventRequest.to_json())

# convert the object into a dict
create_guild_scheduled_event_request_dict = create_guild_scheduled_event_request_instance.to_dict()
# create an instance of CreateGuildScheduledEventRequest from a dict
create_guild_scheduled_event_request_from_dict = CreateGuildScheduledEventRequest.from_dict(create_guild_scheduled_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


