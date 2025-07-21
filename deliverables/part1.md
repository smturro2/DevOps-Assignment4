
## dev
Quick and easy tests to make sure things still work and the changes work as intended
- Data Management:
    - Typically just have dumby data which has reproducible results
- Access:
    - Assessble to main developers of the changes
    - Security not much of a concern since it typically is isolated
- Types of tests:
    - linting
    - Unit tets
    - regression tests
    - Model analytics

## build/integration
- Build your code with all it's dependencies. Main goal is to make sure everything still works together.
- Data Management:
    - Maybe copy prod, or have some dumby data
- Access:
    - Assessble to wider developer teams
    - Not accessible to users or outside firm 
    - Tight security also needed here
- Types of tests:
    - Integration tests
    - regression tests
    - smoke testing
    - End to end model analysis
- smoke testing (measure high level performance)

## staging
- A whole different environment with the changes. The main goal is replicate production environment as much as practial. 
- Data Management:
    - Direct copy of prod
- Access:
    - Accessible to developers, UAT teams, or other teams that may need to sign off / give final inputs
    - Not accessible from users to prevent bad user experience
    - Higher chance of vulnerabilities here tied with access to a prod replica, so security is a big concern
- Testing approaches
    - Performance testing
        - for example stress testing
    - Smoke testing
    - Security testing
    - System wide analytical analysis

## Production
- This is your actual code/environment that users interact with. The main goal is to deliver the code in a bug free experience for the users
- Data Management:
    - Have a roll back strategy
- Access:
    - Accessible from user's pov
    - Not accessible from developers pov to prevent breaking prod
- Testing approaches
    - Live monitoring of prod env is always good
