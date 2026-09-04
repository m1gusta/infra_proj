from pathlib import Path

import yaml
from pydantic import BaseModel, Field

ROOT_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT_DIR / "config" / "infrastructure.yml"


class ProjectConfig(BaseModel):
    name: str
    environment: str


class ApplicationConfig(BaseModel):
    name: str
    port: int = Field(gt=0, le=65535)
    replicas: int = Field(gt=0)


class DeploymentConfig(BaseModel):
    mode: str


class MonitoringConfig(BaseModel):
    enabled: bool


class LoadTestingConfig(BaseModel):
    enabled: bool


class InfrastructureConfig(BaseModel):
    project: ProjectConfig
    application: ApplicationConfig
    deployment: DeploymentConfig
    monitoring: MonitoringConfig
    load_testing: LoadTestingConfig


def load_config() -> InfrastructureConfig:
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    return InfrastructureConfig.model_validate(data)


if __name__ == "__main__":
    config = load_config()
    print("Configuration is valid.")
    print(f"Project: {config.project.name}")
    print(f"Environment: {config.project.environment}")
    print(f"Application: {config.application.name}")
    print(f"Port: {config.application.port}")
    print(f"Replicas: {config.application.replicas}")