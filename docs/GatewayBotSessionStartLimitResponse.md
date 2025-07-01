# GatewayBotSessionStartLimitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_concurrency** | **int** |  | 
**remaining** | **int** |  | 
**reset_after** | **int** |  | 
**total** | **int** |  | 

## Example

```python
from dc_rest.models.gateway_bot_session_start_limit_response import GatewayBotSessionStartLimitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayBotSessionStartLimitResponse from a JSON string
gateway_bot_session_start_limit_response_instance = GatewayBotSessionStartLimitResponse.from_json(json)
# print the JSON string representation of the object
print(GatewayBotSessionStartLimitResponse.to_json())

# convert the object into a dict
gateway_bot_session_start_limit_response_dict = gateway_bot_session_start_limit_response_instance.to_dict()
# create an instance of GatewayBotSessionStartLimitResponse from a dict
gateway_bot_session_start_limit_response_from_dict = GatewayBotSessionStartLimitResponse.from_dict(gateway_bot_session_start_limit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


