# GatewayResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 

## Example

```python
from dc_rest.models.gateway_response import GatewayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GatewayResponse from a JSON string
gateway_response_instance = GatewayResponse.from_json(json)
# print the JSON string representation of the object
print(GatewayResponse.to_json())

# convert the object into a dict
gateway_response_dict = gateway_response_instance.to_dict()
# create an instance of GatewayResponse from a dict
gateway_response_from_dict = GatewayResponse.from_dict(gateway_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


