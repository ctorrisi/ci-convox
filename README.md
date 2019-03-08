# ci-convox

Alpine based image with Convox CLI and custom scripts.

### update-env-vars

```
Usage: update-env-vars org rack [envs]
```
Where:
 * `envs` is a list of optional environment variables to provide to the app
 * `app` is implied by .convox/app or the current working directory

The script resolves differences between the current environment variables and those provided in `envs` and will take the following actions:
* `convox env set` any environment variables provided in `envs` that are either not currently present or whose values differ
* `convox env unset` any environment variables not provided in `envs`
