from atlas_runtime.config.settings import WORKSPACES_PATH


class WorkspaceRuntimeManager:

    def list_workspaces(self):

        result = []

        if not WORKSPACES_PATH.exists():
            return result

        for item in sorted(WORKSPACES_PATH.iterdir()):

            if item.is_dir():

                result.append(
                    {
                        "name": item.name,
                        "path": str(item),
                        "status": "available",
                    }
                )

        return result
