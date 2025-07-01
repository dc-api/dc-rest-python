# GuildAuditLogResponseIntegrationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**name** | **str** |  | [optional] 
**account** | [**AccountResponse**](AccountResponse.md) |  | [optional] 
**application_id** | **str** |  | 

## Example

```python
from dc_rest.models.guild_audit_log_response_integrations_inner import GuildAuditLogResponseIntegrationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GuildAuditLogResponseIntegrationsInner from a JSON string
guild_audit_log_response_integrations_inner_instance = GuildAuditLogResponseIntegrationsInner.from_json(json)
# print the JSON string representation of the object
print(GuildAuditLogResponseIntegrationsInner.to_json())

# convert the object into a dict
guild_audit_log_response_integrations_inner_dict = guild_audit_log_response_integrations_inner_instance.to_dict()
# create an instance of GuildAuditLogResponseIntegrationsInner from a dict
guild_audit_log_response_integrations_inner_from_dict = GuildAuditLogResponseIntegrationsInner.from_dict(guild_audit_log_response_integrations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


