import os
from crewai import Crew
from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks


class TripCrew:

  def __init__(self, origin, cities, date_range, interests):
    self.cities = cities
    self.origin = origin
    self.interests = interests
    self.date_range = date_range

  def run(self):
    agents = CustomAgents()
    tasks = CustomTasks()

    city_selection_agent = agents.city_selection_agent()
    local_tour_guide = agents.local_tour_guide()
    expert_travel_agent = agents.expert_travel_agent()

    identify_task = tasks.identify_task(
      city_selector_agent,
      self.origin,
      self.cities,
      self.interests,
      self.date_range
    )
    gather_task = tasks.gather_task(
      local_expert_agent,
      self.origin,
      self.interests,
      self.date_range
    )
    plan_task = tasks.plan_task(
      travel_concierge_agent, 
      self.origin,
      self.interests,
      self.date_range
    )

    crew = Crew(
      agents=[
        city_selector_agent, local_expert_agent, travel_concierge_agent
      ],
      tasks=[identify_task, gather_task, plan_task],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to Trip Planner Crew")
  print('-------------------------------')
  location = input(
    dedent("""
      From where will you be traveling from?
    """))
  cities = input(
    dedent("""
      What are the cities options you are interested in visiting?
    """))
  date_range = input(
    dedent("""
      What is the date range you are interested in traveling?
    """))
  interests = input(
    dedent("""
      What are some of your high level interests and hobbies?
    """))
  
  trip_crew = TripCrew(location, cities, date_range, interests)
  result = trip_crew.run()
  print("\n\n########################")
  print("## Here is you Trip Plan")
  print("########################\n")
  print(result)
