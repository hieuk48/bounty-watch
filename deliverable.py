"""
bounty_watch_changes.py

Implements logic to track and report bounty watchlist changes,
specifically for the scenario:
  - 0 new
  - 0 resumed
  - 2 watchlist changes

This module is designed to be integrated into the abdulsalam-create/bounty-watch
project, and can be used to generate a summary of bounty watchlist changes.

Constraints:
- No external dependencies.
- Pure Python, secure, and production-ready.
"""

from typing import List, Dict, Any


class BountyWatchChange:
    """
    Represents a single change in the bounty watchlist.
    """
    def __init__(self, issue_id: int, action: str, details: str) -> None:
        """
        Initialize a BountyWatchChange.

        :param issue_id: The unique identifier for the issue.
        :param action: The type of change ('added', 'removed', etc.).
        :param details: Additional details about the change.
        """
        self.issue_id = issue_id
        self.action = action
        self.details = details

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the change to a dictionary.

        :return: Dictionary representation of the change.
        """
        return {
            "issue_id": self.issue_id,
            "action": self.action,
            "details": self.details
        }


class BountyWatchReport:
    """
    Tracks and summarizes bounty watchlist changes.
    """
    def __init__(self) -> None:
        self.new_bounties: List[BountyWatchChange] = []
        self.resumed_bounties: List[BountyWatchChange] = []
        self.watchlist_changes: List[BountyWatchChange] = []

    def add_new_bounty(self, change: BountyWatchChange) -> None:
        """
        Add a new bounty change.

        :param change: The BountyWatchChange instance.
        """
        self.new_bounties.append(change)

    def add_resumed_bounty(self, change: BountyWatchChange) -> None:
        """
        Add a resumed bounty change.

        :param change: The BountyWatchChange instance.
        """
        self.resumed_bounties.append(change)

    def add_watchlist_change(self, change: BountyWatchChange) -> None:
        """
        Add a watchlist change.

        :param change: The BountyWatchChange instance.
        """
        self.watchlist_changes.append(change)

    def summary(self) -> Dict[str, Any]:
        """
        Generate a summary of the changes.

        :return: Dictionary summarizing the changes.
        """
        return {
            "new": len(self.new_bounties),
            "resumed": len(self.resumed_bounties),
            "watchlist_changes": len(self.watchlist_changes),
            "details": {
                "new": [c.to_dict() for c in self.new_bounties],
                "resumed": [c.to_dict() for c in self.resumed_bounties],
                "watchlist_changes": [c.to_dict() for c in self.watchlist_changes]
            }
        }

    def __str__(self) -> str:
        """
        String representation of the summary.

        :return: Human-readable summary.
        """
        return (
            f"{self.summary()['new']} new, "
            f"{self.summary()['resumed']} resumed, "
            f"{self.summary()['watchlist_changes']} watchlist changes"
        )


def example_usage() -> None:
    """
    Example usage of the BountyWatchReport to match the scenario:
    0 new, 0 resumed, 2 watchlist changes.
    """
    report = BountyWatchReport()

    # Simulate two watchlist changes
    change1 = BountyWatchChange(
        issue_id=173,
        action="added_to_watchlist",
        details="Issue #173 added to watchlist"
    )
    change2 = BountyWatchChange(
        issue_id=174,
        action="removed_from_watchlist",
        details="Issue #174 removed from watchlist"
    )

    report.add_watchlist_change(change1)
    report.add_watchlist_change(change2)

    # Print summary
    print(report)
    # For test verification
    assert report.summary()["new"] == 0
    assert report.summary()["resumed"] == 0
    assert report.summary()["watchlist_changes"] == 2
    assert len(report.summary()["details"]["watchlist_changes"]) == 2


if __name__ == "__main__":
    example_usage()