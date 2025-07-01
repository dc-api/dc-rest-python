# GuildAuditLogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_log_entries** | [**List[AuditLogEntryResponse]**](AuditLogEntryResponse.md) |  | 
**users** | [**List[UserResponse]**](UserResponse.md) |  | 
**integrations** | [**List[GuildAuditLogResponseIntegrationsInner]**](GuildAuditLogResponseIntegrationsInner.md) |  | 
**webhooks** | [**List[ListChannelWebhooks200ResponseInner]**](ListChannelWebhooks200ResponseInner.md) |  | 
**guild_scheduled_events** | [**List[ListGuildScheduledEvents200ResponseInner]**](ListGuildScheduledEvents200ResponseInner.md) |  | 
**threads** | [**List[ThreadResponse]**](ThreadResponse.md) |  | 
**application_commands** | [**List[ApplicationCommandResponse]**](ApplicationCommandResponse.md) |  | 
**auto_moderation_rules** | [**List[ListAutoModerationRules200ResponseInner]**](ListAutoModerationRules200ResponseInner.md) |  | 

## Example

```python
from dc_rest.models.guild_audit_log_response import GuildAuditLogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GuildAuditLogResponse from a JSON string
guild_audit_log_response_instance = GuildAuditLogResponse.from_json(json)
# print the JSON string representation of the object
print(GuildAuditLogResponse.to_json())

# convert the object into a dict
guild_audit_log_response_dict = guild_audit_log_response_instance.to_dict()
# create an instance of GuildAuditLogResponse from a dict
guild_audit_log_response_from_dict = GuildAuditLogResponse.from_dict(guild_audit_log_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


