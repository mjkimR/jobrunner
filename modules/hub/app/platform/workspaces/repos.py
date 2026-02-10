from app.platform.workspaces.models import Workspace
from app.platform.workspaces.schemas import WorkspaceCreate, WorkspaceUpdate
from app_base.base.repos.base import BaseRepository


class WorkspaceRepository(BaseRepository[Workspace, WorkspaceCreate, WorkspaceUpdate]):
    model = Workspace
