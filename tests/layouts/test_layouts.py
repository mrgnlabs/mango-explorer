from solana.publickey import PublicKey

import base64

import mango.layouts as layouts


def test_group_layout():
    encoded_group = "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"
    decoded_group = base64.b64decode(encoded_group)

    group = layouts.GROUP.parse(decoded_group)

    # Not an exhaustive check, just a few key areas
    assert group.num_oracles == 10
    assert len(group.tokens) == 16
    assert group.tokens[0].mint == PublicKey("Bb9bsTQa1bGEtQ5KagGkvSHyuLqDWumFUcRqFusFNJWC")
    assert group.tokens[1].mint == PublicKey("3UNBZ6o52WTWwjac2kPUb4FyodhU1vFkRJheu1Sh2TvU")
    assert group.tokens[14].mint is None
    assert group.tokens[15].mint == PublicKey("8FRFC6MoGGkMFQwngccyu69VnYbzykGeez7ignHVAFSN")

    assert len(group.spot_markets) == 15
    assert group.spot_markets[0].spot_market == PublicKey("BqAmk715myHomPTMtuSydqqntQ9PDnJ1WoXMc2oAUomj")
    assert group.spot_markets[9].spot_market == PublicKey("Cyc11qk1FQTmQNFHMHEbwLsgdnHzFK2DrowiKwrGaHxC")
    assert group.spot_markets[14].spot_market is None

    assert len(group.perp_markets) == 15
    assert group.perp_markets[0].perp_market == PublicKey("Gnd9WTaFjJwZU8XEpoB8EYfx5GryJ1dRDw9EzwLtX2b")
    assert group.perp_markets[9].perp_market == PublicKey("6JZZbRjmqCke4Nm9XkzsrXFzM7LdmFHndDA5gcdiRvEx")
    assert group.perp_markets[14].perp_market is None

    assert len(group.oracles) == 15
    assert group.oracles[0] == PublicKey("5mcAUWKEaz1esD8wywy7P79MtBpHKXGU8dvew1YYoPyG")
    assert group.oracles[9] == PublicKey("38xoQ4oeJCBrcVvca2cGk7iV1dAfrmTR1kmhSCJQ8Jto")
    assert group.oracles[14] is None

    assert group.signer_nonce == 0
    assert group.signer_key == PublicKey("9GXvznfEep9yEsvH4CQzqNy5GH81FNk1HDeAR8UjefSf")
    assert group.admin == PublicKey("Cwg1f6m4m3DGwMEbmsbAfDtUToUf5jRdKrJSGD7GfZCB")
    assert group.serum_program_address == PublicKey("DESVgJVGajEgKGXhb6XmqDHGz3VjdgP7rEVESBgxmroY")
    assert group.cache == PublicKey("PJhM2enPpZH7E9wgw7Sqt8S2p4mr3Bc7SycawQwfY7b")
    assert group.valid_interval == 5
    assert group.insurance_vault == PublicKey("14gfuPWjUQnYXpsxs4WgsjafUrJctKkR9AMFH7fjvTgR")
    assert group.srm_vault == PublicKey("23Z3FWjXdt18FiZUwfsnQkUDvF14MneS7uoMYytfNe3G")
    assert group.msrm_vault == PublicKey("Qjf6vWMKPwEMLMM6ci9tudUWZ2t8zVXHqHverDWFx9S")
    assert group.fees_vault is None
