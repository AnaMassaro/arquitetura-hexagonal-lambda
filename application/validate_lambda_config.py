from domain.ports.lambda_data_port import LambdaDataPort


def validate_config(lambda_names: list[str], fetcher: LambdaDataPort) -> dict:
    report = {}

    for name in lambda_names:
        runtime = fetcher.get_runtime(name)
        is_valid = runtime.startswith("python3") and float(runtime[7:]) >= 3.9
        report[name] = {"runtime": runtime, "valid": is_valid}

    return report

