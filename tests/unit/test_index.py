import index
from logs.models.batch_metadata import BatchMetadata

lambda_event = {
    "invocationId": "1545b29a-10ca-4f7f-a60f-54195607c98d",
    "deliveryStreamArn": "arn:aws:firehose:us-east-1:444652832050:deliverystream/b-FirehoseLogStreams-lbcTAGyNE8hz",
    "region": "us-east-1",
    "records": [
        {
            "recordId": "49615192443673540283798383997441439122248557324429950978000000",
            "approximateArrivalTimestamp": 1612438967376,
            "data": "H4sIAAAAAAAAAGWQzWrDMBCEXyXobMNK1urHN0Mc00NODr20ITiOSAy2ZSy5oYS8ezcNOZTCnuabZXfmxgYXQnN2u+/JsZyti11x2JZ1XVQlS5i/jm4mWUqpUJhMAALJvT9Xs18mIm3vl9O1ie3l0C4h+oHY01HH2TUDWQQInoJIQaYkh6ecsLAcQzt3U+z8uOn66ObA8g92TOt/AFL+BusSt0WxeceK7X8PlF9ujI+dG+tOdCdDiwYtIAcUWivNFapMobQKjOFCK4vCaq2NkmiMkBaAyCNQ7KiG2AyUiCsuZGasQq5l8qrnT4wVF7mk0Z+R3li9LPf9/Qf9DEk+TwEAAA=="
        },
        {
            "recordId": "49615192443673540283798383997442648048068174358786342914000000",
            "approximateArrivalTimestamp": 1612439002747,
            "data": "H4sIAAAAAAAAAGWQwWrDMBBEfyXobMNqV5Il3wxxTA85OfTShuA4IjXYlrHkhBDy71Ubcii9vpllZufOBut9c7a722RZztbFrjhsy7ouqpIlzF1HO0cshFASNSFIiLh352p2yxSVtnfL6dqE9uvQLj64IWpPRx1m2wzRgoA8BUxBpBH7J06YX46+nbspdG7cdH2ws2f5Bzum9T8BUv4G61Jui2LzLiu2/w0oL3YMPzd31p1iDkkjtTScgKM22nCugIgMlwozNIoUABlEwUGAFllmSGkhdOwSujhDaIb4EVccBRkAUETJa54/b6w45oJyxM8Qa6xelsf+8Q1mxAG9TwEAAA=="
        },
        {
            "recordId": "49615192443673540283798383997443856973887789262838956034000000",
            "approximateArrivalTimestamp": 1612439006290,
            "data": "H4sIAAAAAAAAAGVQy2qDQBT9lTBrhTt37qjjToiRLrIydNOGYMyQCuqIMyaEkH/vbUMWpdvz4DzuYrDeN2e7u01W5GJd7IrDtqzroipFJNx1tDPDRJRozBSCBoZ7d65mt0zMtL1bTtcmtF+HdvHBDcw9FXWYbTOwBAFlDBgDxQz7JxwJvxx9O3dT6Ny46fpgZy/yD3GM638ExPIN1qXeFsXmXVdi/xtQXuwYfjx30Z04R2mjM22kyjgQETOSqVEqNWDQUKpAJkCQIaSJIkk8JQWpJHKX0PENoRl4kUwkkjIA7Mbodc+fGSuJOakck8/ANVYvyWP/+AbSuZ1nTwEAAA=="
        },
        {
            "recordId": "49615192443673540283798383997445065899707404304330522626000000",
            "approximateArrivalTimestamp": 1612439011420,
            "data": "H4sIAAAAAAAAAGWQwWrDMBBEfyXoHMNqpbW8vhnimB5ycuilDcFxRGqwLWPJDSXk36s25FB6fTPLzM5NDNb75mL3X5MVudgU++K4K+u6qEqxFu462jlirXVKmCkEgoh7d6lmt0xRaXu3nK9NaD+O7eKDG6L2cNRhts0QLQgoE8AEdBKxf+C18MvJt3M3hc6N264PdvYifxOnpP4nQCJfYFPSrii2r1SJw29A+WnH8HNzE9055ihiyoilZmAyBhmMylSapaQptjeGiSRKglRpg8ialUJmjF1CF2cIzRA/kqlErRiApcrWz3n+vLGSmGuVK/keYo3V03I/3L8BezNvmk8BAAA="
        }
    ]
}


def test_read_batch_metadata():
    batch_metadata = index.read_batch_metadata(lambda_event)

    assert vars(batch_metadata) == vars(BatchMetadata("444652832050", "us-east-1", "aws"))