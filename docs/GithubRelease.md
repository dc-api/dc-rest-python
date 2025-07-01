# GithubRelease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**tag_name** | **str** |  | 
**html_url** | **str** |  | 
**author** | [**GithubUser**](GithubUser.md) |  | 

## Example

```python
from dc_rest.models.github_release import GithubRelease

# TODO update the JSON string below
json = "{}"
# create an instance of GithubRelease from a JSON string
github_release_instance = GithubRelease.from_json(json)
# print the JSON string representation of the object
print(GithubRelease.to_json())

# convert the object into a dict
github_release_dict = github_release_instance.to_dict()
# create an instance of GithubRelease from a dict
github_release_from_dict = GithubRelease.from_dict(github_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


