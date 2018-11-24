pragma solidity ^0.4.18;

contract Voting {
  mapping (bytes32 => uint8) public votesReceived;

  bytes32[] public candidateList;

  function Voting(bytes32[] candidateNames) public {
    candidateList = candidateNames;
  }

  function totalVotesForCandidate(bytes32 candidateName) view public returns (uint8) {
    require(validCandidate(candidateName));
    return votesReceived[candidateName];
  }

  function voteForCandidate(bytes32 candidateName) public {
    require(validCandidate(candidateName));
    votesReceived[candidateName] += 1;
  }

  function validCandidate(bytes32 candidateName) view public returns (bool) {
    for (uint8 i = 0; i < candidateList.length; i++) {
      if (candidateList[i] == candidateName) {
        return true;
      }
    }

    return false;
  }
}
