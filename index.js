const web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:8545'));
const abi = JSON.parse(
	'[{"constant":true,"inputs":[{"name":"candidateName","type":"bytes32"}],"name":"validCandidate","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"}],"name":"votesReceived","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"candidateList","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"candidateName","type":"bytes32"}],"name":"totalVotesForCandidate","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"candidateName","type":"bytes32"}],"name":"voteForCandidate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"candidateNames","type":"bytes32[]"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]'
);

const VotingContract = web3.eth.contract(abi);
const contractInstance = VotingContract.at(
	'0xd30de5385b22074569cad04b9aa1a8b671f0bb3f'
);
const candidates = {
	Rama: 'candidate-1',
	Nick: 'candidate-2',
	Jose: 'candidate-3'
};

const candidateNames = Object.keys(candidates);

const updateDivForCandidate = candidateName => {
	const divId = candidates[candidateName];
	const $div = $(`#${divId}`);

	$div.html(contractInstance.totalVotesForCandidate(candidateName).toString());
};

const voteForCandidate = () => {
	const candidateName = $('#candidate').val();
	const opts = { from: web3.eth.accounts[0] };

	contractInstance.voteForCandidate(candidateName, opts, () =>
		updateDivForCandidate(candidateName)
	);
};

$(document).ready(() => candidateNames.forEach(updateDivForCandidate));
