# GithubCheckRunOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.github_check_run_output import GithubCheckRunOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GithubCheckRunOutput from a JSON string
github_check_run_output_instance = GithubCheckRunOutput.from_json(json)
# print the JSON string representation of the object
print(GithubCheckRunOutput.to_json())

# convert the object into a dict
github_check_run_output_dict = github_check_run_output_instance.to_dict()
# create an instance of GithubCheckRunOutput from a dict
github_check_run_output_from_dict = GithubCheckRunOutput.from_dict(github_check_run_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


